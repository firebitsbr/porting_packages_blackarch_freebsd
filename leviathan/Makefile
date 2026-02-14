PORTNAME=	leviathan
DISTVERSION=	35.a1a1d8c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A mass audit toolkit which has wide range service discovery, brute force, SQL injection detection and running custom exploit capabilities.
WWW=		https://github.com/leviathan-framework/leviathan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-google-api-client@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
