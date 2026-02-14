PORTNAME=	hoaxshell
DISTVERSION=	150.e1bba89
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Windows reverse shell payload generator and handler that abuses the http(s) protocol to establish a beacon-like reverse shell.
WWW=		https://github.com/t3l3machus/hoaxshell

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ipython \
		??/py-gnureadline@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
