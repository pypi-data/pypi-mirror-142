from wagtail.core import hooks
from wagtail_colour_picker_enoki.utils.colour import register_all_colour_features


# 1. Use the register_rich_text_features hook.
@hooks.register('register_rich_text_features')
def register_textcolour_feature(features):
    # register all colour features
    register_all_colour_features(features)