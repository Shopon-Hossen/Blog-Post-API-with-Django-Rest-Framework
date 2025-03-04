from tag.models import Tag


def get_or_create_tag(tag_list):
    tag_objs = []
    for name in tag_list:
        lower_name = name.lower()  # Normalize the tag name to lowercase
        tag, created = Tag.objects.get_or_create(name=lower_name)
        tag_objs.append(tag)
    return tag_objs
