PORTNAME=	kubestriker
DISTVERSION=	v1.2.0.r2.ge1776ea
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Blazing fast Security Auditing tool for Kubernetes.
WWW=		https://github.com/vchinnipilli/kubestriker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-virtualenv@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
