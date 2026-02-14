PORTNAME=	leaklooker
DISTVERSION=	5.0d2b9fc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Find open databases with Shodan.
WWW=		https://github.com/woj-ciech/LeakLooker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-hurry-filesize@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
