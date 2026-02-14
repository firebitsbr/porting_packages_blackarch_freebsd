PORTNAME=	zeratool
DISTVERSION=	48.3fb3262
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automatic Exploit Generation (AEG) and remote flag capture for exploitable CTF problems.
WWW=		https://github.com/ChrisTheCoolHut/Zeratool

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/angr \
		??/ipython \
		??/py-claripy@${PY_FLAVOR} \
		??/py-idalink@${PY_FLAVOR} \
		??/py-pwntools@${PY_FLAVOR} \
		??/py-r2pipe@${PY_FLAVOR} \
		??/py-ropper@${PY_FLAVOR} \
		??/py-timeout-decorator@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
