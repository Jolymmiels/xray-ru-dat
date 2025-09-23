# Russian GeoIP Rules

Автоматически генерируемые IP адреса России для маршрутизации в прокси-серверах.

## Файлы правил

### geoip.dat

- Генерируется из данных [MaxMind GeoLite2](https://github.com/Loyalsoldier/geoip) и базы RIPE
- Содержит все IP адреса, назначенные России
- Совместим с [V2Ray](https://github.com/v2fly/v2ray-core), [Xray-core](https://github.com/XTLS/Xray-core), [mihomo](https://github.com/MetaCubeX/mihomo), [hysteria](https://github.com/apernet/hysteria)
- Автоматическая сборка каждый день в 9:00 МСК

## Загрузка файлов

- **geoip.dat**: [Последний релиз](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/geoip.dat)
- **IPv4 списки**: [russian-ipv4-final.txt](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/russian-ipv4-final.txt)
- **IPv6 списки**: [russian-ipv6-final.txt](https://github.com/Loyalsoldier/v2ray-rules-dat/releases/latest/download/russian-ipv6-final.txt)

## Использование

### V2Ray/Xray

```json
{
  "routing": {
    "rules": [
      {
        "type": "field",
        "outboundTag": "direct",
        "ip": ["geoip:ru"]
      }
    ]
  }
}
```

### mihomo/Clash

```yaml
rules:
  - GEOIP,RU,DIRECT
```

### hysteria

```
direct(geoip:ru)
```

## Источники данных

- **MaxMind GeoLite2**: Официальная база географических данных IP адресов
- **RIPE Database**: Европейский реестр интернет-ресурсов для российских диапазонов

## Автоматизация

GitHub Actions выполняет ежедневную сборку:
1. Загрузка данных из MaxMind и RIPE
2. Извлечение российских IP диапазонов
3. Оптимизация и дедупликация
4. Генерация .dat файла
5. Публикация релиза

## Лицензия

Данные предоставляются по лицензии [CC0 1.0 Universal](LICENSE).