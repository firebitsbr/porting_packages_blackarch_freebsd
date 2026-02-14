PORTNAME=	python-selenium-wire
DISTVERSION=	5.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extends Selenium to give you the ability to inspect requests made by the browser.
WWW=		https://pypi.org/project/selenium-wire/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-blinker@${PY_FLAVOR} \
		??/py-brotli@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-h2@${PY_FLAVOR} \
		??/py-hyperframe@${PY_FLAVOR} \
		??/py-kaitaistruct@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-selenium@${PY_FLAVOR} \
		??/py-wsproto@${PY_FLAVOR} \
		??/py-zstandard@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
