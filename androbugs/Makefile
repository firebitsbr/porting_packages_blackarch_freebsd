PORTNAME=	androbugs
DISTVERSION=	7fd3a2c.r0.g7fd3a2c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An efficient Android vulnerability scanner that helps developers or hackers find potential security vulnerabilities in Android applications.
WWW=		https://github.com/AndroBugs/AndroBugs_Framework

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-elfesteem@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-pyside@${PY_FLAVOR} \
		??/radare2 \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
