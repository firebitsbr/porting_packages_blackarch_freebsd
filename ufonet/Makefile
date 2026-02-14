PORTNAME=	ufonet
DISTVERSION=	84.aea21b3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool designed to launch DDoS attacks against a target, using Open Redirect vectors on third party web applications, like botnet.
WWW=		https://github.com/epsylon/ufonet

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/geoip \
		??/py-crypto@${PY_FLAVOR} \
		??/py-geoip@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		??/py-pygeoip@${PY_FLAVOR} \
		??/scapy \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
