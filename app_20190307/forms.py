from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
# ItemFormとはフォームの名前
# forms.ModelFormクラスを継承

    class Meta:
        # このクラス内でDjangoにフォームを作成するときにどのモデルを使えばいいか(model = Item)を伝える
        model = Item

        # フォームのフィールドに何を置くかを以下に書く
        # 使い方参照 https://docs.djangoproject.com/ja/2.1/ref/forms/widgets/
        fields = ('name', 'age', 'sex', 'memo')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'記入例:鈴木　太郎'}),
            'age': forms.NumberInput(attrs={'min':1}),
            # Formをラジオボタンに変更するオブジェクト
            'sex': forms.RadioSelect(),
            'memo': forms.Textarea(attrs={'rows':4}),
        }



