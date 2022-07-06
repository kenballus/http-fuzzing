#!/usr/bin/env bash

for site in www.google.com www.youtube.com facebook.com twitter.com instagram.com baidu.com wikipedia.org yandex.ru yahoo.com whatsapp.com amazon.com yahoo.co live.com netflix.com tiktok.com reddit.com office.com vk.com linkedin.com discord.com zoom.us twitch.tv naver.com bing.com mail.ru roblox.com msn.com duckduckgo.com pinterest.com msn.com news.yahoo.co.jp microsoft.com fandom.com ebay.com globo.com samsung.com weather.com weather.com ok.ru
do
    echo -ne "$site:\t"
    cat test.http | timeout 5 nc $site 80 | grep -E '^HTTP/'
done