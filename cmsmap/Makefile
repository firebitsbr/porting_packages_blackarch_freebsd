PORTNAME=	cmsmap
DISTVERSION=	8.59dd0e2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python open source Content Management System scanner that automates the process of detecting security flaws of the most popular CMSs.
WWW=		https://www.dionach.com/blog/cmsmap-%E2%80%93-a-simple-cms-vulnerability-scanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/exploitdb \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
