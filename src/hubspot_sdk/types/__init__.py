# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import cms, marketing
from .. import _compat
from .file import File as File
from .folder import Folder as Folder
from .option import Option as Option
from .shared import (
    Error as Error,
    Paging as Paging,
    NextPage as NextPage,
    ErrorDetail as ErrorDetail,
    VersionUser as VersionUser,
    PreviousPage as PreviousPage,
    ForwardPaging as ForwardPaging,
    StandardError as StandardError,
    PublicObjectID as PublicObjectID,
    AssociationSpec as AssociationSpec,
    BatchInputString as BatchInputString,
)
from .property import Property as Property
from .file_stat import FileStat as FileStat
from .signed_url import SignedURL as SignedURL
from .option_param import OptionParam as OptionParam
from .associated_id import AssociatedID as AssociatedID
from .settings_response import SettingsResponse as SettingsResponse
from .throttling_settings import ThrottlingSettings as ThrottlingSettings
from .file_action_response import FileActionResponse as FileActionResponse
from .subscription_response import SubscriptionResponse as SubscriptionResponse
from .webhook_create_params import WebhookCreateParams as WebhookCreateParams
from .webhook_update_params import WebhookUpdateParams as WebhookUpdateParams
from .folder_action_response import FolderActionResponse as FolderActionResponse
from .collection_response_file import CollectionResponseFile as CollectionResponseFile
from .webhook_configure_params import WebhookConfigureParams as WebhookConfigureParams
from .throttling_settings_param import ThrottlingSettingsParam as ThrottlingSettingsParam
from .collection_response_folder import CollectionResponseFolder as CollectionResponseFolder
from .folder_update_task_locator import FolderUpdateTaskLocator as FolderUpdateTaskLocator
from .labels_between_object_pair import LabelsBetweenObjectPair as LabelsBetweenObjectPair
from .public_default_association import PublicDefaultAssociation as PublicDefaultAssociation
from .subscription_list_response import SubscriptionListResponse as SubscriptionListResponse
from .webhook_update_batch_params import WebhookUpdateBatchParams as WebhookUpdateBatchParams
from .import_from_url_task_locator import ImportFromURLTaskLocator as ImportFromURLTaskLocator
from .property_modification_metadata import PropertyModificationMetadata as PropertyModificationMetadata
from .multi_associated_object_with_label import MultiAssociatedObjectWithLabel as MultiAssociatedObjectWithLabel
from .batch_response_subscription_response import BatchResponseSubscriptionResponse as BatchResponseSubscriptionResponse
from .subscription_batch_update_request_param import (
    SubscriptionBatchUpdateRequestParam as SubscriptionBatchUpdateRequestParam,
)
from .batch_response_public_default_association import (
    BatchResponsePublicDefaultAssociation as BatchResponsePublicDefaultAssociation,
)
from .created_response_labels_between_object_pair import (
    CreatedResponseLabelsBetweenObjectPair as CreatedResponseLabelsBetweenObjectPair,
)
from .collection_response_multi_associated_object_with_label import (
    CollectionResponseMultiAssociatedObjectWithLabel as CollectionResponseMultiAssociatedObjectWithLabel,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    cms.blogs.blog_post.BlogPost.update_forward_refs()  # type: ignore
    cms.blogs.collection_response_with_total_blog_post_forward_paging.CollectionResponseWithTotalBlogPostForwardPaging.update_forward_refs()  # type: ignore
    cms.blogs.collection_response_with_total_version_blog_post.CollectionResponseWithTotalVersionBlogPost.update_forward_refs()  # type: ignore
    cms.blogs.layout_section.LayoutSection.update_forward_refs()  # type: ignore
    cms.blogs.version_blog_post.VersionBlogPost.update_forward_refs()  # type: ignore
    marketing.collection_response_form_definition_base_forward_paging.CollectionResponseFormDefinitionBaseForwardPaging.update_forward_refs()  # type: ignore
    marketing.datepicker_field.DatepickerField.update_forward_refs()  # type: ignore
    marketing.dependent_field.DependentField.update_forward_refs()  # type: ignore
    marketing.dropdown_field.DropdownField.update_forward_refs()  # type: ignore
    marketing.email_field.EmailField.update_forward_refs()  # type: ignore
    marketing.field_group.FieldGroup.update_forward_refs()  # type: ignore
    marketing.file_field.FileField.update_forward_refs()  # type: ignore
    marketing.hub_spot_form_definition.HubSpotFormDefinition.update_forward_refs()  # type: ignore
    marketing.mobile_phone_field.MobilePhoneField.update_forward_refs()  # type: ignore
    marketing.multi_line_text_field.MultiLineTextField.update_forward_refs()  # type: ignore
    marketing.multiple_checkboxes_field.MultipleCheckboxesField.update_forward_refs()  # type: ignore
    marketing.number_field.NumberField.update_forward_refs()  # type: ignore
    marketing.payment_link_radio_field.PaymentLinkRadioField.update_forward_refs()  # type: ignore
    marketing.phone_field.PhoneField.update_forward_refs()  # type: ignore
    marketing.radio_field.RadioField.update_forward_refs()  # type: ignore
    marketing.single_checkbox_field.SingleCheckboxField.update_forward_refs()  # type: ignore
    marketing.single_line_text_field.SingleLineTextField.update_forward_refs()  # type: ignore
else:
    cms.blogs.blog_post.BlogPost.model_rebuild(_parent_namespace_depth=0)
    cms.blogs.collection_response_with_total_blog_post_forward_paging.CollectionResponseWithTotalBlogPostForwardPaging.model_rebuild(
        _parent_namespace_depth=0
    )
    cms.blogs.collection_response_with_total_version_blog_post.CollectionResponseWithTotalVersionBlogPost.model_rebuild(
        _parent_namespace_depth=0
    )
    cms.blogs.layout_section.LayoutSection.model_rebuild(_parent_namespace_depth=0)
    cms.blogs.version_blog_post.VersionBlogPost.model_rebuild(_parent_namespace_depth=0)
    marketing.collection_response_form_definition_base_forward_paging.CollectionResponseFormDefinitionBaseForwardPaging.model_rebuild(
        _parent_namespace_depth=0
    )
    marketing.datepicker_field.DatepickerField.model_rebuild(_parent_namespace_depth=0)
    marketing.dependent_field.DependentField.model_rebuild(_parent_namespace_depth=0)
    marketing.dropdown_field.DropdownField.model_rebuild(_parent_namespace_depth=0)
    marketing.email_field.EmailField.model_rebuild(_parent_namespace_depth=0)
    marketing.field_group.FieldGroup.model_rebuild(_parent_namespace_depth=0)
    marketing.file_field.FileField.model_rebuild(_parent_namespace_depth=0)
    marketing.hub_spot_form_definition.HubSpotFormDefinition.model_rebuild(_parent_namespace_depth=0)
    marketing.mobile_phone_field.MobilePhoneField.model_rebuild(_parent_namespace_depth=0)
    marketing.multi_line_text_field.MultiLineTextField.model_rebuild(_parent_namespace_depth=0)
    marketing.multiple_checkboxes_field.MultipleCheckboxesField.model_rebuild(_parent_namespace_depth=0)
    marketing.number_field.NumberField.model_rebuild(_parent_namespace_depth=0)
    marketing.payment_link_radio_field.PaymentLinkRadioField.model_rebuild(_parent_namespace_depth=0)
    marketing.phone_field.PhoneField.model_rebuild(_parent_namespace_depth=0)
    marketing.radio_field.RadioField.model_rebuild(_parent_namespace_depth=0)
    marketing.single_checkbox_field.SingleCheckboxField.model_rebuild(_parent_namespace_depth=0)
    marketing.single_line_text_field.SingleLineTextField.model_rebuild(_parent_namespace_depth=0)
