PORTNAME=	volatility-extra
DISTVERSION=	92.d9fc072
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Volatility plugins developed and maintained by the community.
WWW=		https://github.com/volatilityfoundation/community

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pefile@${PY_FLAVOR} \
		??/py-yara@${PY_FLAVOR} \
		??/volatility3 \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
