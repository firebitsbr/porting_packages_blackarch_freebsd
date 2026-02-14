PORTNAME=	dga-detection
DISTVERSION=	78.0a3186e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	DGA Domain Detection using Bigram Frequency Analysis.
WWW=		https://github.com/philarkwright/DGA-Detection

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-alexa-top-sites@${PY_FLAVOR} \
		??/py-argparse@${PY_FLAVOR} \
		??/py-pushbullet.py@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		??/py-websocket-client@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
