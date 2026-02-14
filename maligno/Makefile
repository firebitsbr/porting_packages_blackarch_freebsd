PORTNAME=	maligno
DISTVERSION=	2.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open source penetration testing tool written in python, that serves Metasploit payloads. It generates shellcode with msfvenom and transmits it over HTTP or HTTPS.
WWW=		http://www.encripto.no/tools/

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/metasploit \
		??/py-ipcalc@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
