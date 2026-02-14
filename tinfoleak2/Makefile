PORTNAME=	tinfoleak2
DISTVERSION=	41.c45c33e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The most complete open-source tool for Twitter intelligence analysis.
WWW=		http://www.vicenteaguileradiaz.com/tools/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-exifread@${PY_FLAVOR} \
		??/py-exiv2@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-oauth2@${PY_FLAVOR} \
		??/py-pillow@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-tweepy@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
