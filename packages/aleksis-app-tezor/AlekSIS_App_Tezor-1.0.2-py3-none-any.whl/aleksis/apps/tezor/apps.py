from django.apps import apps
from django.db import OperationalError

from aleksis.core.util.apps import AppConfig
from aleksis.core.util.core_helpers import get_site_preferences


class DefaultConfig(AppConfig):
    name = "aleksis.apps.tezor"
    verbose_name = "AlekSIS — Tezor"
    dist_name = "AlekSIS-App-Tezor"

    urls = {
        "Repository": "https://edugit.org/AlekSIS/onboarding//AlekSIS-App-Tezor",
    }
    licence = "EUPL-1.2+"
    copyright_info = (
        ([2022], "Dominik George", "dominik.george@teckids.org"),
        ([2022], "Tom Teichler", "tom.teichler@teckids.org"),
    )

    def ready(self):
        from django.conf import settings  # noqa

        settings.PAYMENT_VARIANTS = {}

        for app_config in apps.app_configs.values():
            if hasattr(app_config, "get_payment_variants"):
                try:
                    variants = app_config.get_payment_variants()
                except OperationalError:
                    # Non-fatal, database is not yet ready
                    continue
                for name, config in variants.items():
                    if name not in settings.PAYMENT_VARIANTS:
                        settings.PAYMENT_VARIANTS[name] = config

    def get_payment_variants(self):
        prefs = get_site_preferences()
        variants = {}

        if prefs["payments__sofort_api_id"]:
            variants["sofort"] = (
                "payments.sofort.SofortProvider",
                {
                    "id": prefs["payments__sofort_api_id"],
                    "key": prefs["payments__sofort_api_key"],
                    "project_id": prefs["payments__sofort_project_id"],
                    "endpoint": "https://api.sofort.com/api/xml",
                },
            )

        if prefs["payments__paypal_client_id"]:
            variants["paypal"] = (
                "payments.paypal.PaypalProvider",
                {
                    "client_id": prefs["payments__paypal_client_id"],
                    "secret": prefs["payments__paypal_secret"],
                    "capture": not prefs["payments__paypal_capture"],
                    "endpoint": "https://api.paypal.com",
                },
            )

        if prefs["payments__pledge_enabled"]:
            variants["pledge"] = ("djp_sepa.providers.PaymentPledgeProvider", {})

        if prefs["payments__sdd_creditor_identifier"]:
            variants["sdd"] = (
                "djp_sepa.providers.DirectDebitProvider",
                {
                    "creditor": prefs["payments__sdd_creditor"],
                    "creditor_identifier": prefs["payments__sdd_creditor_identifier"],
                },
            )

        return variants
