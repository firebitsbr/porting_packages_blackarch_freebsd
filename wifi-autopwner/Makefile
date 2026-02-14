PORTNAME=	wifi-autopwner
DISTVERSION=	36.faa4d01
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script to automate searching and auditing Wi-Fi networks with weak security.
WWW=		https://github.com/Mi-Al/WiFi-autopwner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/crda \
		??/create_ap \
		??/crunch \
		??/hashcat \
		??/iw \
		??/pixiewps \
		??/reaver \
		??/routersploit \
		??/sipcalc \
		??/wireless-regdb \
		??/wireshark-qt \
		??/wpa_supplicant \
		??/xterm \
		devel/git \
		ftp/curl \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
