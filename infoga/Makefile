PORTNAME=	infoga
DISTVERSION=	33.79a1c03
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool for gathering e-mail accounts information from different public sources (search engines, pgp key servers).
WWW=		https://github.com/m4ll0k/infoga

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
