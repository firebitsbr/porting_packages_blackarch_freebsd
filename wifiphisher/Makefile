PORTNAME=	wifiphisher
DISTVERSION=	799.b11da35
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Fast automated phishing attacks against WPA networks.
WWW=		https://github.com/wifiphisher/wifiphisher

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/aircrack-ng \
		??/dnsmasq \
		??/hostapd \
		??/py-blessings@${PY_FLAVOR} \
		??/py-dbus@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-pbkdf2@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pyric@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		??/roguehostapd \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
