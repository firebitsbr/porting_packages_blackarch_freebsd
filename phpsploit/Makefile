PORTNAME=	phpsploit
DISTVERSION=	1021.aea961d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Stealth post-exploitation framework.
WWW=		https://github.com/nil0x42/phpsploit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-phpserialize@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
