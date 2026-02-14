PORTNAME=	loki-packet
DISTVERSION=	0.3.0.r502
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python based framework implementing many packet generation and attack modules for Layer 2 and 3 protocols.
WWW=		http://c0decafe.de/loki.html

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/autoconf \
		??/automake \
		??/cython2 \
		??/subversion

RUN_DEPENDS=	??/libglade \
		??/openssl-1.0 \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-pylibpcap@${PY_FLAVOR} \
		??/py-urwid@${PY_FLAVOR} \
		??/pygtk \
		lang/python3 \
		net/libdnet \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
