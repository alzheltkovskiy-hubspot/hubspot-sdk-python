# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from hubspot_sdk import HubSpot, AsyncHubSpot
from tests.utils import assert_matches_type
from hubspot_sdk._utils import parse_datetime
from hubspot_sdk.types.marketing import (
    MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestForms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: HubSpot) -> None:
        form = client.marketing.forms.create()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: HubSpot) -> None:
        response = client.marketing.forms.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: HubSpot) -> None:
        with client.marketing.forms.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(object, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: HubSpot) -> None:
        form = client.marketing.forms.update(
            form_id="formId",
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: HubSpot) -> None:
        form = client.marketing.forms.update(
            form_id="formId",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
                "lifecycle_stages": [
                    {
                        "object_type_id": "objectTypeId",
                        "value": "value",
                    }
                ],
            },
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
                "css_class": "cssClass",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                        "default_value": "defaultValue",
                                        "placeholder": "placeholder",
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                            "default_value": "defaultValue",
                            "placeholder": "placeholder",
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                    "rich_text": "richText",
                }
            ],
            legal_consent_options={"type": "none"},
            name="name",
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: HubSpot) -> None:
        response = client.marketing.forms.with_raw_response.update(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: HubSpot) -> None:
        with client.marketing.forms.with_streaming_response.update(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(object, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.marketing.forms.with_raw_response.update(
                form_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: HubSpot) -> None:
        form = client.marketing.forms.list()
        assert_matches_type(MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: HubSpot) -> None:
        form = client.marketing.forms.list(
            after="after",
            archived=True,
            form_types=["hubspot"],
            limit=0,
        )
        assert_matches_type(MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: HubSpot) -> None:
        response = client.marketing.forms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: HubSpot) -> None:
        with client.marketing.forms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(
                MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging, form, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: HubSpot) -> None:
        form = client.marketing.forms.delete(
            "formId",
        )
        assert form is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: HubSpot) -> None:
        response = client.marketing.forms.with_raw_response.delete(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert form is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: HubSpot) -> None:
        with client.marketing.forms.with_streaming_response.delete(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert form is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.marketing.forms.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: HubSpot) -> None:
        form = client.marketing.forms.read(
            form_id="formId",
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: HubSpot) -> None:
        form = client.marketing.forms.read(
            form_id="formId",
            archived=True,
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: HubSpot) -> None:
        response = client.marketing.forms.with_raw_response.read(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: HubSpot) -> None:
        with client.marketing.forms.with_streaming_response.read(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(object, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_read(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.marketing.forms.with_raw_response.read(
                form_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace(self, client: HubSpot) -> None:
        form = client.marketing.forms.replace(
            form_id="formId",
            id="id",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
            },
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                }
            ],
            form_type="hubspot",
            legal_consent_options={"type": "none"},
            name="name",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: HubSpot) -> None:
        form = client.marketing.forms.replace(
            form_id="formId",
            id="id",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
                "lifecycle_stages": [
                    {
                        "object_type_id": "objectTypeId",
                        "value": "value",
                    }
                ],
            },
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
                "css_class": "cssClass",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                        "default_value": "defaultValue",
                                        "placeholder": "placeholder",
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                            "default_value": "defaultValue",
                            "placeholder": "placeholder",
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                    "rich_text": "richText",
                }
            ],
            form_type="hubspot",
            legal_consent_options={"type": "none"},
            name="name",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: HubSpot) -> None:
        response = client.marketing.forms.with_raw_response.replace(
            form_id="formId",
            id="id",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
            },
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                }
            ],
            form_type="hubspot",
            legal_consent_options={"type": "none"},
            name="name",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = response.parse()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: HubSpot) -> None:
        with client.marketing.forms.with_streaming_response.replace(
            form_id="formId",
            id="id",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
            },
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                }
            ],
            form_type="hubspot",
            legal_consent_options={"type": "none"},
            name="name",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = response.parse()
            assert_matches_type(object, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: HubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            client.marketing.forms.with_raw_response.replace(
                form_id="",
                id="id",
                archived=True,
                configuration={
                    "allow_link_to_reset_known_values": True,
                    "archivable": True,
                    "cloneable": True,
                    "create_new_contact_for_new_email": True,
                    "editable": True,
                    "language": "af",
                    "notify_contact_owner": True,
                    "notify_recipients": ["string"],
                    "post_submit_action": {
                        "type": "thank_you",
                        "value": "value",
                    },
                    "pre_populate_known_values": True,
                    "recaptcha_enabled": True,
                },
                created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                display_options={
                    "render_raw_html": True,
                    "style": {
                        "background_width": "backgroundWidth",
                        "font_family": "fontFamily",
                        "help_text_color": "helpTextColor",
                        "help_text_size": "helpTextSize",
                        "label_text_color": "labelTextColor",
                        "label_text_size": "labelTextSize",
                        "legal_consent_text_color": "legalConsentTextColor",
                        "legal_consent_text_size": "legalConsentTextSize",
                        "submit_alignment": "left",
                        "submit_color": "submitColor",
                        "submit_font_color": "submitFontColor",
                        "submit_size": "submitSize",
                    },
                    "submit_button_text": "submitButtonText",
                    "theme": "default_style",
                },
                field_groups=[
                    {
                        "fields": [
                            {
                                "dependent_fields": [
                                    {
                                        "dependent_condition": {
                                            "operator": "eq",
                                            "range_end": "rangeEnd",
                                            "range_start": "rangeStart",
                                            "value": "value",
                                            "values": ["string"],
                                        },
                                        "dependent_field": {
                                            "dependent_fields": [],
                                            "field_type": "phone",
                                            "hidden": True,
                                            "label": "label",
                                            "name": "name",
                                            "object_type_id": "objectTypeId",
                                            "required": True,
                                            "use_country_code_select": True,
                                            "validation": {
                                                "max_allowed_digits": 0,
                                                "min_allowed_digits": 0,
                                            },
                                        },
                                    }
                                ],
                                "field_type": "email",
                                "hidden": True,
                                "label": "label",
                                "name": "name",
                                "object_type_id": "objectTypeId",
                                "required": True,
                                "validation": {
                                    "blocked_email_domains": ["string"],
                                    "use_default_block_list": True,
                                },
                            }
                        ],
                        "group_type": "default_group",
                        "rich_text_type": "text",
                    }
                ],
                form_type="hubspot",
                legal_consent_options={"type": "none"},
                name="name",
                updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            )


class TestAsyncForms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.create()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.forms.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.forms.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(object, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.update(
            form_id="formId",
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.update(
            form_id="formId",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
                "lifecycle_stages": [
                    {
                        "object_type_id": "objectTypeId",
                        "value": "value",
                    }
                ],
            },
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
                "css_class": "cssClass",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                        "default_value": "defaultValue",
                                        "placeholder": "placeholder",
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                            "default_value": "defaultValue",
                            "placeholder": "placeholder",
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                    "rich_text": "richText",
                }
            ],
            legal_consent_options={"type": "none"},
            name="name",
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.forms.with_raw_response.update(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.forms.with_streaming_response.update(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(object, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.marketing.forms.with_raw_response.update(
                form_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.list()
        assert_matches_type(MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.list(
            after="after",
            archived=True,
            form_types=["hubspot"],
            limit=0,
        )
        assert_matches_type(MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.forms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.forms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(
                MarketingFormsCollectionResponseFormDefinitionBaseForwardPaging, form, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.delete(
            "formId",
        )
        assert form is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.forms.with_raw_response.delete(
            "formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert form is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.forms.with_streaming_response.delete(
            "formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert form is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.marketing.forms.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.read(
            form_id="formId",
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.read(
            form_id="formId",
            archived=True,
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.forms.with_raw_response.read(
            form_id="formId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.forms.with_streaming_response.read(
            form_id="formId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(object, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_read(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.marketing.forms.with_raw_response.read(
                form_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.replace(
            form_id="formId",
            id="id",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
            },
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                }
            ],
            form_type="hubspot",
            legal_consent_options={"type": "none"},
            name="name",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncHubSpot) -> None:
        form = await async_client.marketing.forms.replace(
            form_id="formId",
            id="id",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
                "lifecycle_stages": [
                    {
                        "object_type_id": "objectTypeId",
                        "value": "value",
                    }
                ],
            },
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
                "css_class": "cssClass",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                        "default_value": "defaultValue",
                                        "placeholder": "placeholder",
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                            "default_value": "defaultValue",
                            "placeholder": "placeholder",
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                    "rich_text": "richText",
                }
            ],
            form_type="hubspot",
            legal_consent_options={"type": "none"},
            name="name",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            archived_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncHubSpot) -> None:
        response = await async_client.marketing.forms.with_raw_response.replace(
            form_id="formId",
            id="id",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
            },
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                }
            ],
            form_type="hubspot",
            legal_consent_options={"type": "none"},
            name="name",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        form = await response.parse()
        assert_matches_type(object, form, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncHubSpot) -> None:
        async with async_client.marketing.forms.with_streaming_response.replace(
            form_id="formId",
            id="id",
            archived=True,
            configuration={
                "allow_link_to_reset_known_values": True,
                "archivable": True,
                "cloneable": True,
                "create_new_contact_for_new_email": True,
                "editable": True,
                "language": "af",
                "notify_contact_owner": True,
                "notify_recipients": ["string"],
                "post_submit_action": {
                    "type": "thank_you",
                    "value": "value",
                },
                "pre_populate_known_values": True,
                "recaptcha_enabled": True,
            },
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            display_options={
                "render_raw_html": True,
                "style": {
                    "background_width": "backgroundWidth",
                    "font_family": "fontFamily",
                    "help_text_color": "helpTextColor",
                    "help_text_size": "helpTextSize",
                    "label_text_color": "labelTextColor",
                    "label_text_size": "labelTextSize",
                    "legal_consent_text_color": "legalConsentTextColor",
                    "legal_consent_text_size": "legalConsentTextSize",
                    "submit_alignment": "left",
                    "submit_color": "submitColor",
                    "submit_font_color": "submitFontColor",
                    "submit_size": "submitSize",
                },
                "submit_button_text": "submitButtonText",
                "theme": "default_style",
            },
            field_groups=[
                {
                    "fields": [
                        {
                            "dependent_fields": [
                                {
                                    "dependent_condition": {
                                        "operator": "eq",
                                        "range_end": "rangeEnd",
                                        "range_start": "rangeStart",
                                        "value": "value",
                                        "values": ["string"],
                                    },
                                    "dependent_field": {
                                        "dependent_fields": [],
                                        "field_type": "phone",
                                        "hidden": True,
                                        "label": "label",
                                        "name": "name",
                                        "object_type_id": "objectTypeId",
                                        "required": True,
                                        "use_country_code_select": True,
                                        "validation": {
                                            "max_allowed_digits": 0,
                                            "min_allowed_digits": 0,
                                        },
                                    },
                                }
                            ],
                            "field_type": "email",
                            "hidden": True,
                            "label": "label",
                            "name": "name",
                            "object_type_id": "objectTypeId",
                            "required": True,
                            "validation": {
                                "blocked_email_domains": ["string"],
                                "use_default_block_list": True,
                            },
                        }
                    ],
                    "group_type": "default_group",
                    "rich_text_type": "text",
                }
            ],
            form_type="hubspot",
            legal_consent_options={"type": "none"},
            name="name",
            updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            form = await response.parse()
            assert_matches_type(object, form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncHubSpot) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `form_id` but received ''"):
            await async_client.marketing.forms.with_raw_response.replace(
                form_id="",
                id="id",
                archived=True,
                configuration={
                    "allow_link_to_reset_known_values": True,
                    "archivable": True,
                    "cloneable": True,
                    "create_new_contact_for_new_email": True,
                    "editable": True,
                    "language": "af",
                    "notify_contact_owner": True,
                    "notify_recipients": ["string"],
                    "post_submit_action": {
                        "type": "thank_you",
                        "value": "value",
                    },
                    "pre_populate_known_values": True,
                    "recaptcha_enabled": True,
                },
                created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
                display_options={
                    "render_raw_html": True,
                    "style": {
                        "background_width": "backgroundWidth",
                        "font_family": "fontFamily",
                        "help_text_color": "helpTextColor",
                        "help_text_size": "helpTextSize",
                        "label_text_color": "labelTextColor",
                        "label_text_size": "labelTextSize",
                        "legal_consent_text_color": "legalConsentTextColor",
                        "legal_consent_text_size": "legalConsentTextSize",
                        "submit_alignment": "left",
                        "submit_color": "submitColor",
                        "submit_font_color": "submitFontColor",
                        "submit_size": "submitSize",
                    },
                    "submit_button_text": "submitButtonText",
                    "theme": "default_style",
                },
                field_groups=[
                    {
                        "fields": [
                            {
                                "dependent_fields": [
                                    {
                                        "dependent_condition": {
                                            "operator": "eq",
                                            "range_end": "rangeEnd",
                                            "range_start": "rangeStart",
                                            "value": "value",
                                            "values": ["string"],
                                        },
                                        "dependent_field": {
                                            "dependent_fields": [],
                                            "field_type": "phone",
                                            "hidden": True,
                                            "label": "label",
                                            "name": "name",
                                            "object_type_id": "objectTypeId",
                                            "required": True,
                                            "use_country_code_select": True,
                                            "validation": {
                                                "max_allowed_digits": 0,
                                                "min_allowed_digits": 0,
                                            },
                                        },
                                    }
                                ],
                                "field_type": "email",
                                "hidden": True,
                                "label": "label",
                                "name": "name",
                                "object_type_id": "objectTypeId",
                                "required": True,
                                "validation": {
                                    "blocked_email_domains": ["string"],
                                    "use_default_block_list": True,
                                },
                            }
                        ],
                        "group_type": "default_group",
                        "rich_text_type": "text",
                    }
                ],
                form_type="hubspot",
                legal_consent_options={"type": "none"},
                name="name",
                updated_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            )
