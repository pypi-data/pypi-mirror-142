from django.urls import reverse, path, include
from django.utils.html import format_html
from django.utils.translation import ugettext as _

from wagtail.admin.rich_text.editors.draftail import features as draftail_features
from wagtail.core import hooks

from wagtail_colour_picker_enoki.conf import get_setting
from wagtail_colour_picker_enoki.utils.colour import register_all_colour_features


@hooks.register('register_admin_urls')
def register_admin_urls():
    from wagtail_colour_picker_enoki import urls
    return [
        path('wagtail_colour_picker_enoki/', include((urls, 'wagtail_colour_picker_enoki'))),
    ]


@hooks.register('insert_editor_js')
def insert_editor_js():
    js_includes = format_html(
        "<script>window.chooserUrls.colourChooser = '{0}';</script>",
        reverse('wagtail_colour_picker_enoki:chooser')
    )
    return js_includes


@hooks.register('register_rich_text_features')
def register_textcolour_feature(features):
    # register all colour features
    register_all_colour_features(features)

    # register the color picker
    feature_name = 'textcolour'
    type_ = feature_name.upper()

    control = {
        'type': type_,
        'label': 'labelColor',
        'description': 'Text Colour',
    }

    features.register_editor_plugin(
        'draftail',
        feature_name,
        draftail_features.EntityFeature(
            control,
            js=[
                'colourpicker/js/chooser.js',
                'colourpicker/js/colourpicker.js',
            ],
            css={
                'all': ['colourpicker/css/colourpicker.css'],
            }
        )
    )

    features.default_features.append(feature_name)