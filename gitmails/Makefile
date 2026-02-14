PORTNAME=	gitmails
DISTVERSION=	0.1.1.r6.g8aa8411
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An information gathering tool to collect git commit emails in version control host services.
WWW=		https://github.com/giovanifss/gitmails

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pygit2@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
