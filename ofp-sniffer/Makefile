PORTNAME=	ofp-sniffer
DISTVERSION=	1.0.0.r89.g0d907da
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An OpenFlow sniffer to help network troubleshooting in production networks.
WWW=		https://github.com/amlight/ofp_sniffer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dateutil@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-hexdump@${PY_FLAVOR} \
		??/py-influxdb@${PY_FLAVOR} \
		??/py-openflow@${PY_FLAVOR} \
		??/py-pcapy@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
