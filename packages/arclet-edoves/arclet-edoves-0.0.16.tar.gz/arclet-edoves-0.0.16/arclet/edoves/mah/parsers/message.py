from typing import Dict, cast

from arclet.edoves.builtin.medium import DictMedium
from arclet.edoves.main.parser import BaseDataParser, ParserBehavior, ParserMetadata
from ..protocol import MAHProtocol
from ..chain import MessageChain


class NudgeOperateMeta(ParserMetadata):
    parser_targets = "NudgeSend", "NudgeEvent"


class MessageActionMeta(ParserMetadata):
    parser_targets = (
        "MessageSend",
        "MessageGet",
        "MessageRevoke",
        "FriendMessage",
        "GroupMessage",
        "TempMessage",
        "StrangerMessage",
        "GroupRecallEvent",
        "FriendRecallEvent",
    )


class NudgeParserBehavior(ParserBehavior):
    async def from_docker(self, protocol: MAHProtocol, data: DictMedium):
        operator_id = str(data.content.pop('fromId'))
        target_id = str(data.content.pop('target'))
        operator = protocol.scene.monomer_map.get(f"{operator_id}@{protocol.identifier}")
        subject = data.content.pop('subject')
        if subject['kind'] == "Group":
            if not operator or not getattr(operator.metadata, "group_id", None):
                info = await protocol.docker.behavior.session_handle(
                    "get",
                    "memberInfo",
                    {
                        "sessionKey": protocol.docker.metadata.session_key,
                        "target": subject['id'], "memberId": operator_id
                    }
                )
                operator = protocol.include_member(info)
                group = protocol.include_group(info.get("group"))
                if not group.get_child(operator_id):
                    group.set_child(operator)
                operator.metadata.update_data("group_id", group.metadata.pure_id)
            else:
                operator.set_prime_tag("Member")
        elif subject['kind'] == "Friend":
            if not operator:
                profile = await protocol.docker.behavior.session_handle(
                    "get",
                    "friendProfile",
                    {
                        "sessionKey": protocol.docker.metadata.session_key,
                        "target": operator_id
                    }
                )
                profile.setdefault("id", operator_id)
                operator = protocol.include_friend(profile)
            else:
                operator.set_prime_tag("Friend")
        target = protocol.scene.monomer_map.get(f"{target_id}@{protocol.identifier}") or target_id
        await protocol.post_notice(
            "NoticeMe",
            operator,
            self.io.metadata.select_type,
            {**data.content, "target": target}
        )

    async def to_docker(self, protocol: MAHProtocol, data: DictMedium):
        rest = data.content.get('rest')
        source_type = rest.get('type')
        subject = target = data.content.get("target")
        sender = protocol.scene.monomer_map.get(f"{target}@{protocol.identifier}")
        kind = sender.prime_tag
        if source_type:
            if source_type.startswith("Friend") and sender.compare("Friend"):
                kind = "Friend"
            elif source_type.startswith("Group") and sender.compare("Member"):
                if sender.parents:
                    subject = sender.metadata.group_id
                    kind = "Group"
        else:
            if sender.prime_tag == "Member":
                if sender.parents:
                    subject = sender.metadata.group_id
                    kind = "Group"
        await protocol.docker.behavior.session_handle(
            "post",
            "sendNudge",
            {
                "sessionKey": protocol.docker.metadata.session_key,
                "target": target,
                "subject": subject,
                "kind": kind
            }
        )
        protocol.scene.edoves.logger.info(
            f"{protocol.scene.protagonist.metadata.pure_id}: "
            f"{kind}({target}) <- Nudge"
        )


class MessageActionParserBehavior(ParserBehavior):

    async def to_docker(self, protocol: MAHProtocol, data: DictMedium):
        action = data.type
        target = data.content.get("target")
        if action.endswith("Send"):
            sender = protocol.scene.monomer_map.get(f"{target}@{protocol.identifier}")
            rest = data.content.get('rest')
            source_type = rest.get('type')
            if source_type:
                if source_type.startswith("Friend") and sender.compare("Friend"):
                    action = "sendFriendMessage"
                elif source_type.startswith("Group") and sender.compare("Member"):
                    if sender.parents:
                        target = sender.metadata.group_id
                        action = "sendGroupMessage"
            else:
                if sender.prime_tag == "Member":
                    if sender.parents:
                        target = sender.metadata.group_id
                        action = "sendGroupMessage"
                elif sender.prime_tag == "Group":
                    action = "sendGroupMessage"
                elif sender.prime_tag == "Friend":
                    action = "sendFriendMessage"
            message = cast(MessageChain, data.content.get("content")).replace_type("Text", "Plain")
            resp: Dict = await protocol.docker.behavior.session_handle(
                "post",
                action,
                {
                    "sessionKey": protocol.docker.metadata.session_key,
                    "target": target,
                    "messageChain": message.dict()["__root__"],
                    **(
                        {"quote": rest.get("quote")} if data.content.get("reply") else {}
                    )

                }
            )
            resp['id'] = target
            data.send_response(
                DictMedium().create(
                    purveyor=sender,
                    content=resp,
                    medium_type=action.replace('send', '').replace('Message', '')
                )
            )
        elif action.endswith("Revoke"):
            await protocol.docker.behavior.session_handle(
                "post",
                "recall",
                {
                    "sessionKey": protocol.docker.metadata.session_key,
                    "target": target,
                }
            )
        elif action.endswith("Get"):
            message = await protocol.docker.behavior.session_handle(
                "get",
                "messageFromId",
                {
                    "sessionKey": protocol.docker.metadata.session_key,
                    "id": target
                }
            )
            data.send_response(message)

    async def from_docker(self, protocol: MAHProtocol, data: DictMedium):
        ev_type: str = self.io.metadata.select_type
        sender_data: Dict = data.content.get("sender")
        if ev_type.endswith("Message"):
            if ev_type.startswith("Friend"):
                sender = protocol.include_friend(sender_data)
            elif ev_type.startswith("Group") or ev_type.startswith("Temp"):
                sender = protocol.include_member(sender_data)
                group = protocol.include_group(sender_data.get("group"))
                if not group.get_child(sender.metadata.pure_id):
                    group.set_child(sender)
                sender.metadata.update_data("group_id", group.metadata.pure_id)
            else:
                sender = protocol.include_temporary_monomer(sender_data.get("nickname"), str(sender_data.get('id')))
            await protocol.post_message(
                "MessageReceived",
                sender,
                ev_type,
                data.content.get("messageChain")
            )
        elif ev_type.endswith("RecallEvent"):
            call = await protocol.push_medium(
                DictMedium().create(
                    protocol.scene.protagonist,
                    {
                        "target": data.content.pop('messageId'),
                    },
                    "MessageGet"
                )
            )
            await self.to_docker(protocol, await protocol.get_medium())
            message = await call.wait_response()
            if ev_type.startswith("Friend"):
                if not (operator := protocol.scene.monomer_map.get(
                        f"{data.content.pop('operator')}@{protocol.identifier}"
                )):
                    return
            else:
                group_data = data.content.pop('group')
                group = protocol.include_group(group_data)
                operator_data = data.content.pop('operator')
                operator = protocol.include_member(operator_data)
                if not group.get_child(operator.metadata.pure_id):
                    group.set_child(operator)
                operator.metadata.update_data("group_id", group.metadata.pure_id)
            await protocol.post_message(
                "MessageRevoked",
                operator,
                ev_type,
                message['messageChain']
            )


@MAHProtocol.register_parser
class NudgeEventParser(BaseDataParser):
    prefab_metadata = NudgeOperateMeta
    prefab_behavior = NudgeParserBehavior


@MAHProtocol.register_parser
class MessageEventParser(BaseDataParser):
    prefab_metadata = MessageActionMeta
    prefab_behavior = MessageActionParserBehavior
