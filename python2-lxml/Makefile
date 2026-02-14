PORTNAME=	python2-lxml
DISTVERSION=	4.6.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Powerful and Pythonic XML processing library combining libxml2/libxslt with the ElementTree API.
WWW=		https://pypi.org/project/lxml/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cython2 \
		??/py-pygments@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		textproc/libxslt

RUN_DEPENDS=	lang/python3 \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
