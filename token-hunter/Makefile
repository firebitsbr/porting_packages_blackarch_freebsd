PORTNAME=	token-hunter
DISTVERSION=	343.3358a33
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT Tool - Search the group and group members snippets, issues, and issue discussions for sensitive data that may be included in these assets.
WWW=		https://github.com/GitLab-Red-Team/token-hunter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-coloredlogs@${PY_FLAVOR} \
		??/py-furl@${PY_FLAVOR} \
		??/py-requests-mock@${PY_FLAVOR} \
		??/py-retry@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
