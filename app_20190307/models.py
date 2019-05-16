from django.db import models
from django.core import validators

# Create your models here.

class Item(models.Model):
    sex_choices = (
        (1, '男性'),
        (2, '女性')
    )

    name = models.CharField(
        verbose_name = '名前',
        max_length = 200,
    )

    age = models.IntegerField(
        verbose_name = '年齢',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )

    sex = models.IntegerField(
        verbose_name='性別',
        choices=sex_choices,
        default=1,
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length = 300,
        blank = True,
        null = True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'

        # これが管理サイトの文字として表示される
        verbose_name_plural = 'hoge'






