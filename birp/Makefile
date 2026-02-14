PORTNAME=	birp
DISTVERSION=	65.b2e108a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool that will assist in the security assessment of mainframe applications served over TN3270.
WWW=		https://github.com/sensepost/birp

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/fontconfig \
		??/ipython2 \
		??/py-backports.functools_lru_cache@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-igenutils@${PY_FLAVOR} \
		??/py-py3270@${PY_FLAVOR} \
		??/x3270 \
		??/xorg-mkfontdir \
		??/xorg-mkfontscale \
		??/xorg-xset \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
