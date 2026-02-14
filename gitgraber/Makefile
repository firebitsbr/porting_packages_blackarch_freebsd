PORTNAME=	gitgraber
DISTVERSION=	82.aab4839
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Monitor GitHub to search and find sensitive data in real time for different online services.
WWW=		https://github.com/hisxo/gitGraber

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argcomplete@${PY_FLAVOR} \
		??/py-crontab@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
