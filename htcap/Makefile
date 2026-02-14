PORTNAME=	htcap
DISTVERSION=	155.a59c592
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A web application analysis tool for detecting communications between javascript and the server.
WWW=		https://github.com/segment-srl/htcap

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/phantomjs \
		??/py-simplejson@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
