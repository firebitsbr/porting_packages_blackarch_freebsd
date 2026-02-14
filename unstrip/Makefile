PORTNAME=	unstrip
DISTVERSION=	13.05e00c2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	ELF Unstrip Tool.
WWW=		https://github.com/pzread/unstrip

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-pyelftools@${PY_FLAVOR} \
		??/sqlite3 \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
