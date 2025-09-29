#!/usr/bin/env python3

import urllib.request
import json

def get_private_ranges():
    """Get bogon IP ranges"""
    bogon_networks = [
        # IPv4 bogons
        "0.0.0.0/8",
        "10.0.0.0/8",
        "100.64.0.0/10",
        "127.0.0.0/8",
        "169.254.0.0/16",
        "172.16.0.0/12",
        "192.0.0.0/24",
        "192.0.2.0/24",
        "192.88.99.0/24",
        "192.168.0.0/16",
        "198.18.0.0/15",
        "198.51.100.0/24",
        "203.0.113.0/24",
        "224.0.0.0/4",
        "240.0.0.0/4",
        "255.255.255.255/32",

        # IPv6 bogons
        "::/128",
        "::1/128",
        "64:ff9b::/96",
        "100::/64",
        "2001::/32",
        "2001:10::/28",
        "2001:db8::/32",
        "fc00::/7",
        "fe80::/10",
        "ff00::/8",
    ]

    with open('private-ranges.txt', 'w') as f:
        for range_str in bogon_networks:
            f.write(f"{range_str}\n")

    print(f"Created private ranges file with {len(bogon_networks)} ranges")
    return bogon_networks

def get_telegram_ranges():
    """Get Telegram IP ranges"""
    telegram_ranges = []

    # From Telegram's official documentation
    known_telegram_ranges = [
        "149.154.160.0/20",
        "149.154.164.0/22",
        "149.154.168.0/22",
        "149.154.172.0/22",
        "91.108.4.0/22",
        "91.108.8.0/22",
        "91.108.12.0/22",
        "91.108.16.0/22",
        "91.108.20.0/22",
        "91.108.56.0/22",
        "95.161.64.0/20",
        "2001:b28:f23c::/48",
        "2001:b28:f23d::/48",
        "2001:b28:f23f::/48",
        "2001:67c:4e8::/48"
    ]

    telegram_ranges.extend(known_telegram_ranges)

    with open('telegram-ranges.txt', 'w') as f:
        for range_str in telegram_ranges:
            f.write(f"{range_str}\n")

    print(f"Created Telegram ranges file with {len(telegram_ranges)} ranges")
    return telegram_ranges

def get_facebook_ranges():
    """Get Facebook IP ranges"""
    facebook_ranges = []

    try:
        # Facebook provides their IP ranges via API
        with urllib.request.urlopen('https://graph.facebook.com/facebook_ips') as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                facebook_ranges.extend(data.get('ipv4_cidrs', []))
                facebook_ranges.extend(data.get('ipv6_cidrs', []))
    except Exception as e:
        print(f"Could not fetch Facebook ranges from API: {e}")

        # Fallback to known Facebook/Meta ranges
        known_facebook_ranges = [
            "31.13.24.0/21",
            "31.13.64.0/18",
            "31.13.68.0/22",
            "31.13.72.0/21",
            "31.13.80.0/20",
            "31.13.96.0/19",
            "66.220.144.0/20",
            "66.220.160.0/19",
            "69.63.176.0/20",
            "69.171.224.0/19",
            "74.119.76.0/22",
            "103.4.96.0/22",
            "129.134.0.0/17",
            "157.240.0.0/17",
            "173.252.64.0/19",
            "173.252.96.0/19",
            "179.60.192.0/22",
            "185.60.216.0/22",
            "204.15.20.0/22",
            "2a03:2880::/32",
            "2620:0:1c00::/40",
            "2620:0:1cff::/48",
            "2a03:2880:f000::/36"
        ]
        facebook_ranges.extend(known_facebook_ranges)

    with open('facebook-ranges.txt', 'w') as f:
        for range_str in facebook_ranges:
            f.write(f"{range_str}\n")

    print(f"Created Facebook ranges file with {len(facebook_ranges)} ranges")
    return facebook_ranges

def main():
    private_ranges = get_private_ranges()
    telegram_ranges = get_telegram_ranges()
    facebook_ranges = get_facebook_ranges()

    print("\nSummary:")
    print(f"- Private ranges: {len(private_ranges)}")
    print(f"- Telegram ranges: {len(telegram_ranges)}")
    print(f"- Facebook ranges: {len(facebook_ranges)}")

if __name__ == "__main__":
    main()