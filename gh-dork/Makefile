PORTNAME=	gh-dork
DISTVERSION=	3.799f86f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Github dorking tool.
WWW=		https://github.com/molly/gh-dork

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-github3.py@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
