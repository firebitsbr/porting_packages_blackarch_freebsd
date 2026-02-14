PORTNAME=	adexplorersnapshot
DISTVERSION=	142.b8dde33
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	AD Explorer snapshot parser.
WWW=		https://github.com/c3c/ADExplorerSnapshot.py

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/bloodhound-python \
		??/certipy \
		??/py-dissect.cstruct@${PY_FLAVOR} \
		??/py-frozendict@${PY_FLAVOR} \
		??/py-pwntools@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
