PORTNAME=	python-catalogue
DISTVERSION=	2.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library that makes it easy to add function (or object) registries to your code.
WWW=		https://pypi.org/project/catalogue/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/mypy \
		??/py-pytest@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		??/py-zipp@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
