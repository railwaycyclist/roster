from django_filters import filters
from django_filters import FilterSet
from .models import Item

# 並べ替えの指定をするためのクラス
class MyOrderingFilter(filters.OrderingFilter):
    descending_fmt = '%s (降順)'

# 検索機能を追加するクラス
class ItemFilter(FilterSet):

    # lookup_exprで検索条件を部分一致などに変更可能
    name = filters.CharFilter(label='氏名', lookup_expr='contains')
    memo = filters.CharFilter(label='備考', lookup_expr='contains')

    order_by = MyOrderingFilter(
        #tuple-mapping retains order

        fields=(
            ('name', 'name'),
            ('age', 'age'),

        ),

        field_labels={
            'name': '氏名',
            'age': '年齢',
        },
        label='並び順'
    )

    class Meta:

        model = Item
        fields = ('name', 'sex', 'memo')



