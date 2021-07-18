from django.db import models
from django.utils.translation import gettext_lazy as _


class BCBlock(models.Model):
    height = models.BigIntegerField(_('Высота блока'))
    block_hash = models.CharField(_('Хеш блока'), max_length=64)
    timestamp = models.BigIntegerField(_('Время блока'))
    miner_address = models.CharField(_('Адрес майнера'), max_length=34, help_text=_('Его публичный хеш'))
    transaction_quantity = models.IntegerField(_('Количество транзакций'))

    class Meta:
        db_table = 'blockchain_block'
        verbose_name = _('Блок блокчейна')
        verbose_name_plural = _('Блоки блокчейна')
        ordering = ['-timestamp']
