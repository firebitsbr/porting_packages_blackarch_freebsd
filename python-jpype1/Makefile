PORTNAME=	python-jpype1
DISTVERSION=	1.6.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python to Java bridge, an effort to allow Python programs full access to Java class libraries.
WWW=		https://github.com/jpype-project/jpype

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/java-runtime \
		??/py-packaging@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
