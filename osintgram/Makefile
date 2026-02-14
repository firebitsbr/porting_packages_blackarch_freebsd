PORTNAME=	osintgram
DISTVERSION=	1.3.r14.gc8ba1f0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT tool offering an interactive shell to perform analysis on Instagram account of any users by its nickname.
WWW=		https://github.com/Datalux/Osintgram

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-geopy@${PY_FLAVOR} \
		??/py-gnureadline@${PY_FLAVOR} \
		??/py-instagram-private-api@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-requests-toolbelt@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
