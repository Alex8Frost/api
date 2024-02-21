from djchoices import DjangoChoices, ChoiceItem


class TaskPriority(DjangoChoices):
    one = ChoiceItem('1', '1')
    two = ChoiceItem('2', '2')
    three = ChoiceItem('3', '3')