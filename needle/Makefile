PORTNAME=	needle
DISTVERSION=	579.891b660
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The iOS Security Testing Framework.
WWW=		https://github.com/mwrlabs/needle

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/mitmproxy \
		??/py-biplist@${PY_FLAVOR} \
		??/py-frida@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysqlite@${PY_FLAVOR} \
		??/py-sshtunnel@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
