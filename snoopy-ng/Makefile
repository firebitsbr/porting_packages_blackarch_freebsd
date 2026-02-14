PORTNAME=	snoopy-ng
DISTVERSION=	128.eac73f5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A distributed, sensor, data collection, interception, analysis, and
WWW=		https://github.com/sensepost/snoopy-ng

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/autossh \
		??/gpsd \
		??/iw \
		??/mitmproxy \
		??/ppp \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-dnslib@${PY_FLAVOR} \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-publicsuffix@${PY_FLAVOR} \
		??/py-pybluez@${PY_FLAVOR} \
		??/py-pyinotify@${PY_FLAVOR} \
		??/py-pylibpcap@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		??/py-smspdu@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/sqlite3 \
		??/tcpdump \
		lang/python3 \
		net/libpcap \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
