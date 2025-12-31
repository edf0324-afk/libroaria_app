from django.db import models


class PerfumeReview(models.Model):
    
    PERFUME_CHOICES = [
        ('純白の物語', '純白の物語'),
        ('夜明けの読書', '夜明けの読書'),
        ('秘密の書斎', '秘密の書斎'),
        ('雨の図書室', '雨の図書室'),
        ('月夜の詩集', '月夜の詩集'),
        ('湖畔の画集', '湖畔の画集'),
        ('恋の序章', '恋의序章'),
        ('夕暮れの物語', '夕暮れの物語'),
        ('葡萄色の日記', '葡萄色の日記'),
        ('飴色の文学', '飴色の文学'),
    ]
    perfume_name = models.CharField(
        max_length=100,
        choices=PERFUME_CHOICES,
        verbose_name="香水名"
    )
    
    content = models.TextField(verbose_name="香りの感想")
    
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.perfume_name