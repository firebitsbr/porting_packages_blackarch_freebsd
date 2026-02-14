PORTNAME=	facebot
DISTVERSION=	23.57f6025
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A facebook profile and reconnaissance system.
WWW=		https://github.com/pun1sh3r/facebot

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/cookiejar \
		??/mysql-python \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-binaryornot@${PY_FLAVOR} \
		??/py-configparser@${PY_FLAVOR} \
		??/py-cookiecutter@${PY_FLAVOR} \
		??/py-facepy@${PY_FLAVOR} \
		??/py-gdata@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-multipartposthandler@${PY_FLAVOR} \
		??/py-pager@${PY_FLAVOR} \
		??/py-wsgiref@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
