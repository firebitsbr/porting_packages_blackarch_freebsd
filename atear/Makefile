PORTNAME=	atear
DISTVERSION=	139.245ec8d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Wireless Hacking, WiFi Security, Vulnerability Analyzer, Pentestration.
WWW=		https://github.com/NORMA-Inc/AtEar

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/hostapd \
		??/py-flask@${PY_FLAVOR} \
		??/py-libnmap@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-pyodbc@${PY_FLAVOR} \
		??/py-smartencoding@${PY_FLAVOR} \
		??/wireshark-cli \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR} \
		security/nmap \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
