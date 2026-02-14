PORTNAME=	dns2geoip
DISTVERSION=	0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A simple python script that brute forces DNS and subsequently geolocates the found subdomains.
WWW=		http://packetstormsecurity.com/files/118036/DNS-2-GeoIP.html

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		??/py-geoip@${PY_FLAVOR} \
		??/py-simplekml@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
