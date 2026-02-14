PORTNAME=	barq
DISTVERSION=	35.6f1a68c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An AWS Cloud Post Exploitation framework.
WWW=		https://github.com/Voulnet/barq

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-boto3@${PY_FLAVOR} \
		??/py-clint@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
