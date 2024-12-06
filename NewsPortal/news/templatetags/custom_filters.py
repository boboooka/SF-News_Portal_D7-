from django import template

register = template.Library()

BAD_WORDS = ['редиска', 'чушпан', 'редиски']

@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Фильтр применяется только к строкам!')
    # value = value.lower()
    for word in BAD_WORDS:
        if word in value:
            value = value.replace(word, '*'*len(word))
    return value