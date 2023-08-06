from __future__ import annotations

import argparse
import logging
from typing import Any, Optional

from annoworkapi.resource import Resource as AnnoworkResource

import annoworkcli
from annoworkcli.common.cli import build_annoworkapi, get_list_from_args

logger = logging.getLogger(__name__)


class DeleteOrganizationMember:
    def __init__(
        self,
        annowork_service: AnnoworkResource,
        organization_id: str,
    ):
        self.annowork_service = annowork_service
        self.organization_id = organization_id

    def main(self, user_id_list: list[str]):
        organization_members = self.annowork_service.api.get_organization_members(self.organization_id)
        member_dict: dict[str, dict[str, Any]] = {m["user_id"]: m for m in organization_members}
        success_count = 0

        logger.info(f"{len(user_id_list)} 件のユーザを組織メンバから削除します。")
        for user_id in user_id_list:
            member = member_dict.get(user_id)
            if member is None:
                logger.warning(f"{user_id=}: ユーザが組織メンバに存在しません。")
                continue

            try:
                organization_member_id = member["organization_member_id"]
                self.annowork_service.api.delete_organization_member(
                    self.organization_id, organization_member_id=organization_member_id
                )
                success_count += 1
            except Exception as e:
                logger.warning(f"{user_id=}: 組織メンバの削除に失敗しました。{e}")
                continue

        logger.info(f"{success_count}/{len(user_id_list)} 件のユーザを組織メンバから削除しました。")


def main(args):
    annowork_service = build_annoworkapi(args)

    user_id_list = get_list_from_args(args.user_id)
    assert user_id_list is not None
    DeleteOrganizationMember(
        annowork_service=annowork_service,
        organization_id=args.organization_id,
    ).main(user_id_list=user_id_list)


def parse_args(parser: argparse.ArgumentParser):
    parser.add_argument(
        "-org",
        "--organization_id",
        type=str,
        required=True,
        help="対象の組織ID",
    )

    parser.add_argument(
        "-u",
        "--user_id",
        type=str,
        nargs="+",
        required=True,
        help="組織メンバに追加するuser_id",
    )

    parser.set_defaults(subcommand_func=main)


def add_parser(subparsers: Optional[argparse._SubParsersAction] = None) -> argparse.ArgumentParser:
    subcommand_name = "delete"
    subcommand_help = "組織メンバを削除します。"

    parser = annoworkcli.common.cli.add_parser(
        subparsers, subcommand_name, subcommand_help, description=subcommand_help
    )
    parse_args(parser)
    return parser
